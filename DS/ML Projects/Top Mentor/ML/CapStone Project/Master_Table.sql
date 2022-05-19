#Transaction and Loans table
create  table loan_trans #1670
select td.*,ln.loan_id,ln.date as loan_date,ln.amount as loan_amount,ln.duration,ln.payments,ln.status from loan ln join transaction_data td on ln.account_id=td.account_id; #1670

#Account and Orders table(inner join)
create table acc_ord #7213 card_disp_client_dist (d id)
select o.*,acc.date as account_date,acc.district_id as account_district_id,acc.frequency from account acc left join `order` o on acc.account_id=o.account_id; #7213

#Card and Disposition table(inner join)
create table card_disp
select c.*,disp.account_id,disp.client_id as disposition_client_id,disp.type as disposition_type from card c join disposition disp on c.disp_id=disp.disp_id; #892

#card and disposition combine with Client table based on client_id(inner join)
create table card_disp_clent
select * from card_disp cd join client c on cd.disposition_client_id=c.client_id; #892

#card, Dispositon,client table with district Table based on district id(inner join)
create table card_disp_client_dist
select * from card_disp_clent cdc join districtcsv dist on cdc.district_id=dist.A1;

#account,order table with card,disposition,client,district table based on account id(left join)
create table acc_ord_card_disp_client_dist  #7213
select cdcd.*,ao.order_id,ao.bank_to,ao.account_to,ao.amount,ao.k_symbol,ao.account_date,ao.account_district_id,ao.frequency from acc_ord ao left join card_disp_client_dist cdcd on ao.account_id=cdcd.account_id;

#join account,order,card,disposition,client,district with loan,transaction table based on account_id(inner join)
select * from acc_ord_card_disp_client_dist aocdcd join loan_trans lt on lt.account_id= aocdcd.account_id #868